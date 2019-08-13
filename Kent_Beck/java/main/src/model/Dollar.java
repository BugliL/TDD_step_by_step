package model;

public class Dollar extends Money {

    public Dollar(double amount, String currency) {
        super(amount, currency);
    }

    public Money times(int multiplier) {
        return Money.dollar(this.amount * multiplier);
    }

    @Override
    public String currency() {
        return currency;
    }

}
