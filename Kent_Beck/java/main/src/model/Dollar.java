package model;

public class Dollar extends Money {

    private String currency;

    public Dollar(double amount) {
        this.amount = amount;
        currency = "USD";
    }

    public Money times(int multiplier) {
        return new Dollar(this.amount * multiplier);
    }

    @Override
    public String currency() {
        return currency;
    }

}
