package model;

public class Dollar extends Money {

    public Dollar(double amount, String currency) {
        this.currency = currency;
        this.amount = amount;
    }

    public Money times(int multiplier) {
        return Money.dollar(this.amount * multiplier);
    }

    @Override
    public String currency() {
        return currency;
    }

}
