package model;

public class Franc extends Money {

    private String currency;

    public Franc(double amount) {
        this.amount = amount;
        currency = "CHF";
    }

    public Money times(int multiplier) {
        return new Franc(this.amount * multiplier);
    }

    @Override
    public String currency() {
        return currency;
    }

}
