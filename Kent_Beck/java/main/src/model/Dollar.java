package model;

public class Dollar extends Money {

    public Dollar(double amount) {
        this.amount = amount;
    }

    public Dollar times(int multiplier) {
        return new Dollar(this.amount * multiplier);
    }

    @Override
    public boolean equals(Object obj) {
        if (obj == null || obj.getClass() != this.getClass())
            return false;

        Dollar dollar = (Dollar) obj;
        return dollar.amount == this.amount;
    }
}
