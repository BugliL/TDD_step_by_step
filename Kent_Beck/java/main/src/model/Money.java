package model;

public class Money {
    protected double amount;
    protected String currency;

    public static Money dollar(double amount) {
        return new Dollar(amount, "USD");
    }

    public static Money franc(double amount) {
        return new Franc(amount, "CHF");
    }

    public String currency() {
        return this.currency;
    }

    public Money times(int multiplier) {
        return new Money(this.amount * multiplier, this.currency);
    }

    public Money(double amount, String currency) {
        this.amount = amount;
        this.currency = currency;
    }

    @Override
    public boolean equals(Object obj) {
        Money money = (Money) obj;
        return money.amount == this.amount
                && money.currency == this.currency;
    }

    public String toString() {
        return amount + " " + currency;
    }
}
