from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime, time, date
import numbers

class PowerMeter:
    def __init__(
        self,
        tariff1: numbers.Number = 6.5,
        tariff2: numbers.Number = 3.0,
        tariff2_starts: time = time(23, 0),
        tariff2_ends: time = time(6, 0)
    ):
        self.tariff1 = Decimal(tariff1)
        self.tariff2 = Decimal(tariff2)
        self.tariff2_starts = tariff2_starts
        self.tariff2_ends = tariff2_ends
        self.power = Decimal('0.0')
        self.charges = {}
    
    def __repr__(self) -> str:
        """Машиночитаемое представление."""
        return f"<PowerMeter: {self.power:.1f} кВт/ч>"
    
    def __str__(self) -> str:
        """Человекочитаемое представление."""
        total = sum(self.charges.values())
        current_month = datetime.now().strftime("%b")
        return f"({current_month}) {total:.2f}"
    
    def meter(self, power: numbers.Number) -> Decimal:
        """Вычисляет стоимость потреблённой мощности и обновляет начисления."""
        power = Decimal(power)
        current_time = datetime.now().time()
        
        # Определение текущего тарифа
        if self.tariff2_starts < self.tariff2_ends:
            is_tariff2 = self.tariff2_starts <= current_time < self.tariff2_ends
        else:
            is_tariff2 = current_time >= self.tariff2_starts or current_time < self.tariff2_ends
        
        tariff = self.tariff2 if is_tariff2 else self.tariff1
        cost = (power * tariff).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        
        # Обновление общего потребления
        self.power += power
        
        # Обновление начислений
        first_of_month = date(datetime.now().year, datetime.now().month, 1)
        if first_of_month not in self.charges:
            self.charges[first_of_month] = Decimal('0.0')
        self.charges[first_of_month] += cost
        
        return cost
        
#pm1 = PowerMeter()
#pm1.meter(2)
#Decimal('13.00')
#pm1.meter(1.2)
#Decimal('7.80')
#pm1
#<PowerMeter: 3.2 кВт/ч>
#(Jan) 20.80
