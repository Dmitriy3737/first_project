from django.http import JsonResponse
from django.views import View
from .models import User, Balance
from .serializers import BalanceSerializer

class CreditView(View):
    def post(self, request):
        username = request.POST.get('username')
        amount = request.POST.get('amount')

        user, created = User.objects.get_or_create(username=username)
        balance, created = Balance.objects.get_or_create(user=user)
        balance.amount += float(amount)
        balance.save()

        balance_serializer = BalanceSerializer(balance)
        return JsonResponse(balance_serializer.data, status=200)

