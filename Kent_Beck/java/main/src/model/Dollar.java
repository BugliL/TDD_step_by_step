package model;

public class Dollar extends Money {

    public Dollar(double amount) {
        this.amount = amount;
    }

    public Money times(int multiplier) {
        return new Dollar(this.amount * multiplier);
    }

}
