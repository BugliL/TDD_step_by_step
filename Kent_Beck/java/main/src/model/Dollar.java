package model;

public class Dollar {
    public double amount;

    public Dollar(double amount) {
        this.amount = amount;
    }

    public Dollar times(int multiplier) {
        return new Dollar(this.amount * multiplier);
    }
}
