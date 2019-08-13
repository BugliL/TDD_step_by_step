package model;

public abstract class Money {
    protected double amount;
    protected String currency;


    public abstract Money times(int multiplier);

    public static Money dollar(double amount) {
        return new Dollar(amount, "USD");
    }

    public static Money franc(double amount) {
        return new Franc(amount, "CHF");
    }

    public abstract String currency();

    @Override
    public boolean equals(Object obj) {
        if (obj == null || obj.getClass() != this.getClass())
            return false;

        Money money = (Money) obj;
        return money.amount == this.amount;
    }

    public String toString() {
        return amount + " " + currency;
    }
}