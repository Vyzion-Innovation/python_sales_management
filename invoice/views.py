import json

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Invoice
from .serializers import InvoiceSerializer

class InvoiceCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()

        # Extract the raw string (we now expect 'items' key from frontend)
        raw_items_str = data.get("items")
        items = []

        if raw_items_str:
            try:
                # valid_json_str = f"[{raw_items_str}]"
                items = json.loads(raw_items_str)
            except json.JSONDecodeError as e:
                return Response(
                    {"error": f"Invalid JSON in items: {str(e)}"},
                    status=status.HTTP_400_BAD_REQUEST
                )

        # Convert QueryDict to regular dict
        final_data = {
            key: value[0] if isinstance(value, list) else value
            for key, value in request.data.lists()
        }
        final_data["items"] = items  # override with actual list

        serializer = InvoiceSerializer(data=final_data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InvoiceDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, invoice_number):
        try:
             invoice = Invoice.objects.get(invoice_number=invoice_number, user=request.user)
             serializer = InvoiceSerializer(invoice)
             return Response(serializer.data)
        except Invoice.DoesNotExist:
                return Response({"error": "Invoice not found"}, status=status.HTTP_404_NOT_FOUND)