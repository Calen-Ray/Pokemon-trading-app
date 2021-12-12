from django.core.management.base import BaseCommand
import requests
from budget.models import Income_expenses

data = [
    {
        'income' : '5k-10k',
        'housing' : 9357,
        'grocery' : 2247,
        'transportation' : 3211,
        'healthcare' : 1562,
        'misc' : 430,
    },
    {
        'income' : '10k-15k',
        'housing' : 9693,
        'grocery' : 2577,
        'transportation' : 3131,
        'healthcare' : 1989,
        'misc' : 275,
    },
    {
        'income' : '15k-20k',
        'housing' : 10762,
        'grocery' : 2485,
        'transportation' : 3900,
        'healthcare' : 2423,
        'misc' : 509,
    },
    {
        'income' : '20k-30k',
        'housing' : 12409,
        'grocery' : 3037,
        'transportation' : 5717,
        'healthcare' : 3351,
        'misc' : 466,
    },
    {
        'income' : '30k-40k',
        'housing' : 14851,
        'grocery' : 3588,
        'transportation' : 7459,
        'healthcare' : 4038,
        'misc' : 614,
    },
    {
        'income' : '40k-50k',
        'housing' : 18274,
        'grocery' : 3152,
        'transportation' : 8359,
        'healthcare' : 4518,
        'misc' : 813,
    },
    {
        'income' : '50k-70k',
        'housing' : 18274,
        'grocery' : 3864,
        'transportation' : 10377,
        'healthcare' : 4673,
        'misc' : 877,
    },
    {
        'income' : '70k-80k',
        'housing' : 19595,
        'grocery' : 4254,
        'transportation' : 11415,
        'healthcare' : 5176,
        'misc' : 1007,
    },
    {
        'income' : '80k-100k',
        'housing' : 21726,
        'grocery' : 4867,
        'transportation' : 12153,
        'healthcare' : 5611,
        'misc' : 1027,
    },
    {
        'income' : '100k-120k',
        'housing' : 24375,
        'grocery' : 5417,
        'transportation' : 14646,
        'healthcare' : 5934,
        'misc' : 1256,
    },
    {
        'income' : '120k-150k',
        'housing' : 27895,
        'grocery' : 5691,
        'transportation' : 16961,
        'healthcare' : 6727,
        'misc' : 1493,
    },
    {
        'income' : '150k+',
        'housing' : 40561,
        'grocery' : 7122,
        'transportation' : 19394,
        'healthcare' : 7765,
        'misc' : 2106,
    },
]


class Command(BaseCommand):

    def handle(self, *args, **options):



        for income_class in data:
            new_income = Income_expenses()
            new_income.income = income_class['income']
            new_income.grocery = income_class['grocery']
            new_income.housing = income_class['housing']
            new_income.transportation = income_class['transportation']
            new_income.healthcare = income_class['healthcare']
            new_income.misc = income_class['misc']
            new_income.save()
            print(f'new income made, {new_income.income}')