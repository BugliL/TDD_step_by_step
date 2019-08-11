package model;

public class Dollar {
    public double amount;

    public Dollar(double amount) {
        this.amount = amount;
    }

    public void times(int value) {
        this.amount *= value;
    }
}
