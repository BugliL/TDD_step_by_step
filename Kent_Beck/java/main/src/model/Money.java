package model;

public abstract class Money {
    protected double amount;

    public abstract Money times(int multiplier);

    public static Money dollar(double amount){
        return new Dollar(amount);
    }

    public static Money franc(double amount){
        return new Franc(amount);
    }

    @Override
    public boolean equals(Object obj) {
        if (obj == null || obj.getClass() != this.getClass())
            return false;

        Money money = (Money) obj;
        return money.amount == this.amount;
    }
}
