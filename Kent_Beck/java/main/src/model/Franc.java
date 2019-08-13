package model;

public class Franc extends Money {

    public Franc(double amount) {
        this.amount = amount;
    }

    public Franc times(int multiplier) {
        return new Franc(this.amount * multiplier);
    }

}
