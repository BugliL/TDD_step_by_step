package model;

public class Franc {
    private double amount;

    public Franc(double amount) {
        this.amount = amount;
    }

    public Franc times(int multiplier) {
        return new Franc(this.amount * multiplier);
    }


    @Override
    public boolean equals(Object obj) {
        if (obj == null || obj.getClass() != this.getClass()) {
            return false;
        }

        Franc franc_obj = (Franc) obj;
        return franc_obj.amount == this.amount;
    }
}
