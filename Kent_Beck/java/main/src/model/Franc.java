package model;

public class Franc extends Money {

    private String currency;

    public Franc(double amount, String currency) {
        this.amount = amount;
        this.currency = currency;
    }

    public Money times(int multiplier) {
        return new Franc(this.amount * multiplier, "CHF");
    }

    @Override
    public String currency() {
        return currency;
    }

}
