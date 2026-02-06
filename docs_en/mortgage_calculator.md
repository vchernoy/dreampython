# Project: Mortgage Calculator

## Mortgage Calculator: namedtuple, custom types, operator overloading (May 16)

Let's take an educational example: calculating interest and payments for a fixed-rate mortgage. Suppose the house price is $500,000, down payment: 20%. This can be expressed with the following Python code:
```py
home_price = USD * 500000
down_payment = home_price * 0.2
mortgage = home_price - down_payment

print(f'{home_price=}')
print(f'{down_payment=}')
print(f'{mortgage=}')

loan_to_value = mortgage / home_price

print(f'{loan_to_value=:.1%}')
```
Here we also calculated LTV, which in this example will be: 80% (well, since the down payment is: 20%).

We haven't defined USD yet, but you can guess, we're talking about $1, so USD * 500000 means: $500,000.
We'll analyze the missing piece of code a bit later, but for now let's look at the output of this code.

Output:
```
home_price=$500,000.00
down_payment=$100,000.00
mortgage=$400,000.00

loan_to_value=80.0%
```
Magically, numbers are formatted as prices, although the print command itself doesn't seem to do this.
Let's define that the loan is taken at 5% per annum for 30 years. Recalculate into percentage for one month. Also introduce the concept of amortization term which means the loan term in number of months:
```py
mortgage_rate = 0.05
monthly_rate = (1 + mortgage_rate) ** (1 / 12) - 1

print(f'{mortgage_rate=:.1%}')
print(f'{monthly_rate=:.3%}')

mortgage_term = 30
amortization_term = mortgage_term * 12
```
Output:
```
mortgage_rate=5.0%
monthly_rate=0.407%
```
Now we calculate payments both for interest and loan repayment. The calculations are hidden in a function, which we'll analyze a bit later.
```py
monthly_interest, monthly_principle = payment(mortgage, amortization_term, monthly_rate)
monthly_payment = monthly_interest + monthly_principle
print(f'{monthly_interest=}')
print(f'{monthly_principle=}')
print(f'{monthly_payment=}')
```
Output:
```py
monthly_interest=$1,629.65
monthly_principle=$490.57
monthly_payment=$2,120.22
```
Again magic: prices are formatted correctly!

### The `payment()` Function

Here's the missing function for calculating loan payments:
```py
def payment(balance: Dollar, term: int, rate: float) -> tuple[Dollar, Dollar]:
    interest = balance * rate
    principle = interest / ((1 + rate) ** term - 1)

    return interest, principle
```
Calculates using known formulas and returns a pair (tuple): interest payment and loan repayment. Together we get the (monthly) payment. Actually, this function doesn't care whether we're talking about months or years. It uses abstract: balance, term, rate!
Simplifying, suppose the loan balance is $400K, annual interest: 5%, loan for 30 years, then the function payment($400,000, 30, 5%) will calculate:
```py
interest = $400,000 * 5% = $20,000
principle = $20,000 / (1.05^30 - 1) = $6,020
```
Total payment (per year): $5,000 + $1,505 = $26,020.

In terms of whole years, the answer won't be quite correct. It would be more correct to recalculate by months. That's exactly why we call this function as payment($400,000, 12*30, 0.407%).
Note that the function has type annotations and for balance the Dollar type is specified, which we haven't defined anywhere yet.

### The `Dollar` Type

Dollar ⏤ is a class that inherits all fields and properties from another type collections.namedtuple. We could do without inheritance, but namedtuple is a very useful type that you should get acquainted with.

The namedtuple type allows defining named tuples. Dollar ⏤ is exactly a tuple of just one, but named component: amount. Like regular tuples, namedtuple is also immutable ⏤ another useful property.

Of course we can use namedtuple directly, for example like this:
```py
Dollar = namedtuple('Dollar', 'amount', defaults=(1,))
```
Here we define a new type: an immutable named tuple with field amount (with default value: 1). But this is not enough if we want to perform arithmetic operations with objects of type Dollar.

Therefore Dollar inherits the amount field and immutability properties, but defines its own operators. 
For example:
* `__mul__()` helps override the multiplication operator of a Dollar value by some number. 
The result of multiplication will be a Dollar value. \
This allows writing such code: Dollar(500) * 10 ⏤ we get: Dollar(5000).

* The `__add__()` method allows writing such code: Dollar(500) + Dollar(80) ⏤ we get: Dollar(580).

* The `__truediv__()` method allows calculating:
```py
Dollar(500) / Dollar(10) = 50 or
Dollar(500) / 50 = Dollar(10).
```
* The `__str__()` method nicely formats Dollar type objects, and here appears: $5,000 instead of 5000.

```py
from collections import namedtuple
```
```py
class Dollar(namedtuple('Dollar', 'amount', defaults=(1,))):
    def __mul__(self, other: Union[int, float]) -> 'Dollar':
        return Dollar(self.amount * other)

    def __truediv__(self, other: Union[int, float, 'Dollar']) -> 'Dollar':
        return self.amount / other.amount \
        if type(other) == Dollar \
        else Dollar(self.amount / other)

    def __add__(self, other: 'Dollar') -> 'Dollar':
        return Dollar(self.amount + other.amount)

    def __sub__(self, other: 'Dollar') -> 'Dollar':
        return Dollar(self.amount - other.amount)

    def __str__(self) -> str:
        return f'${self.amount:,.2f}' \
        if self.amount >= 0 \
        else f'-${-self.amount:,.2f}'

    def __repr__(self) -> str:
        return str(self)
```
Now we can introduce the missing dollar:
```py
USD = Dollar(1)
```
Code: https://onlinegdb.com/EySDwsUIo

---

## Backend on FastAPI: mortgage calculator (May 23)

In the `webapptest` folder, let's create a project. There we'll save:
* file `main.py` and
* directory `venv` (`virtualenv`).

First of all, install the necessary libraries. Copy the following command into the terminal:
```sh
venv/bin/pip install "fastapi[all]" "uvicorn[standard]"
```
Check what's installed there with the command:
```sh
venv/bin/pip list
```

### `main.py` and starting the WEB service:

We create a backend and register the API. Remember decorators?
```py
import fastapi

app = fastapi.FastAPI()

@app.get("/")
def read_root():
    return 'loan calculator'
```
The `@app.get("/")` decorator sets up a remote call endpoint for the read_root() function, which simply returns a string (nothing fancy!).

Start the service locally, for example, on port 8000:
```sh
venv/bin/uvicorn main:app --reload --port 8000
```
Output:
```
INFO:     Will watch for changes in these directories: ['/Users/slava/PycharmProjects/webapptest']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [29735] using watchgod
INFO:     Started server process [29737]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
If everything is good, let it run!

Now through a web browser you can call the read_root function by typing the following URL:

http://127.0.0.1:8000/

In the browser should appear:
```
"loan calculator"
```
We just started a minimal WEB service (backend)!

### Loan Calculator

Already familiar with named tuples? LoanPayments objects will contain information about payments for a certain period. For example, for one month, a year, the entire period, etc.:
```py
import collections
```
```py
LoanPayments = collections.namedtuple(
    'LoanPayments',
    [
        'interest',
        'principle',
        'paid',
        'balance_left',
        'payments_done',
    ],
)
```
Create an object of this type like this:
```py
loan_payments = LoanPayments(
    interest=1000,
    principle=2000,
    paid=1000+2000,
    balance_left=100000 - 3000,
    payments_done=1,
)
```
The main function that calculates loan payments for a given interval:
```py
def payment(balance: float, term: int, rate: float, payments: int = 1) -> LoanPayments:

    print(f'payment({balance=}, {term=}, {rate=}: {payments=})')

    total_interest, total_principle = 0, 0
    for _ in range(payments):
        interest = balance * rate
        principle = interest / ((1 + rate) ** term - 1)

        total_interest += interest
        total_principle += principle

        balance -= principle
        term -= 1

    return LoanPayments(
        interest=round(total_interest, 2),
        principle=round(total_principle, 2),
        paid=round(total_interest+total_principle, 2),
        balance_left=round(balance, 2),
        payments_done=payments,
    )
```
Input parameters for the function:
* balance: loan debt size, for example: 100000 ($100K).
* term: remaining number of payments, for example: 30 * 12 (30 years).
* rate: credit rate for one payment.
* payments: number of payments, you can specify for example: 1 (month), 12 (year), 120 (10 years) or term (for the entire time).

Add API:
```py
@app.get("/amortization_loan/")
def amortization_loan(balance: float, months_left: int, annual_rate: float, months_to_pay: int = 1):

    annual_rate *= 0.01
    rate = (1 + annual_rate) ** (1 / 12) - 1

    monthly = payment(balance, months_left, rate, 1)
    annual = payment(balance, months_left, rate, 12)
    total = payment(balance, months_left, rate, months_left)
    paid = payment(balance, months_left, rate, months_to_pay)

    return {
        'monthly': monthly._asdict(),
        'annual': annual._asdict(),
        'total': total._asdict(),
        'paid': paid._asdict(),
    }
```
Now in the browser you can specify this URL:

http://127.0.0.1:8000/amortization_loan/?balance=100000&months_left=360&annual_rate=5&months_to_pay=120

Which means: call the amortization_loan function with parameters:
* balance=100000 ($100K);
* months_left=360 (loan for 30 years);
* annual_rate=5 (5% per annum);
* months_to_pay=120 (interested in payments for 10 years).

In the browser we'll get a response in JSON format:
```json
{"monthly":{"interest":407.41,"principle":122.64,"paid":530.06,"balance_left":99877.36,"payments_done":1},"annual":{"interest":4855.52,"principle":1505.14,"paid":6360.66,"balance_left":98494.86,"payments_done":12},"total":{"interest":90819.87,"principle":100000.0,"paid":190819.87,"balance_left":0.0,"payments_done":360},"paid":{"interest":44675.09,"principle":18931.53,"paid":63606.62,"balance_left":81068.47,"payments_done":120}}
```
New API added, the loan calculator service works!

The next step can be skipped:

### JSON Formatting

JSON can be nicely formatted using the module call: python3 -m json.tool. Run the following command in the terminal:
```sh
echo '{"monthly":{"interest":407.41,"principle":122.64,"paid":530.06,"balance_left":99877.36,"payments_done":1},"annual":{"interest":4855.52,"principle":1505.14,"paid":6360.66,"balance_left":98494.86,"payments_done":12},"total":{"interest":90819.87,"principle":100000.0,"paid":190819.87,"balance_left":0.0,"payments_done":360},"paid":{"interest":44675.09,"principle":18931.53,"paid":63606.62,"balance_left":81068.47,"payments_done":120}}' | python3 -m json.tool
```
Output:
```json
{
    "monthly": {
        "interest": 407.41,
        "principle": 122.64,
        "paid": 530.06,
        "balance_left": 99877.36,
        "payments_done": 1
    },
    "annual": {
        "interest": 4855.52,
        "principle": 1505.14,
        "paid": 6360.66,
        "balance_left": 98494.86,
        "payments_done": 12
    },
    "total": {
        "interest": 90819.87,
        "principle": 100000.0,
        "paid": 190819.87,
        "balance_left": 0.0,
        "payments_done": 360
    },
    "paid": {
        "interest": 44675.09,
        "principle": 18931.53,
        "paid": 63606.62,
        "balance_left": 81068.47,
        "payments_done": 120
    }
}
```
* Per month we'll pay: $530;
* per year: $6,360;
* for all 30 years: $190,819;
* for 10 years: $63,606.

### Interactive API docs

FastAPI also generates an endpoint for interactive API. While your service is running, type the following URL in the browser:

http://127.0.0.1:8000/docs

A page should be generated for calling two functions: `Root Read` and `Amortization Loan`.

Click on the arrows and then on "Try it out" and "Execute"!

We got a very simple UI through which we can interact with the service

Full Code: https://onlinegdb.com/7FLyB8K7P

See https://fastapi.tiangolo.com/

