package model;

import org.junit.jupiter.params.shadow.com.univocity.parsers.annotations.Convert;

public class Money {
    protected double amount;
    protected String currency;

    public static Money dollar(double amount) {
        return new Money(amount, "USD");
    }

    public static Money franc(double amount) {
        return new Money(amount, "CHF");
    }

    public String currency() {
        return this.currency;
    }

    public Money times(int multiplier) {
        return new Money(this.amount * multiplier, this.currency);
    }

    public Money(double amount, String currency) {
        this.amount = amount;
        this.currency = currency;
    }

    @Override
    public boolean equals(Object obj) {
        Money money = (Money) obj;
        return money.amount == this.amount
                && money.currency.equals(this.currency);
    }

    public String toString() {
        return amount + " " + currency;
    }

    public Money plus(Money otherMoney) {
        Money money = Converter.to_currency(this.currency, otherMoney);
        return new Money(money.amount + this.amount, this.currency);
    }
}
