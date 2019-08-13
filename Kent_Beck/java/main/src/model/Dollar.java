package model;

public class Dollar extends Money {

    private String currency;

    public Dollar(double amount, String currency) {
        this.amount = amount;
        this.currency = currency;
    }

    public Money times(int multiplier) {
        return Money.dollar(this.amount * multiplier);
    }

    @Override
    public String currency() {
        return currency;
    }

}
