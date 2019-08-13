package model;

public class Franc extends Money {

    public Franc(double amount, String currency) {
        super(amount, currency);
    }

    public Money times(int multiplier) {
        return Money.franc(this.amount * multiplier);
    }

    @Override
    public String currency() {
        return currency;
    }

}
