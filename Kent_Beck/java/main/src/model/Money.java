package model;

public abstract class Money {
    protected double amount;

    @Override
    public boolean equals(Object obj) {
        if (obj == null || obj.getClass() != this.getClass())
            return false;

        Money money = (Money) obj;
        return money.amount == this.amount;
    }
}
