package model;

import java.util.ArrayList;
import java.util.HashMap;

public class Converter {

    private static HashMap<String, HashMap<String, Double>> convertion_table;

    static {
        HashMap<String, Double> chf = new HashMap<>();
        chf.put("CHF", 1d);
        chf.put("USD", 0.5d);

        HashMap<String, Double> usd = new HashMap<>();
        usd.put("USD", 1d);
        usd.put("CHF", 2d);

        convertion_table = new HashMap<>();
        convertion_table.put("CHF", chf);
        convertion_table.put("USD", usd);
    }

    public static Money to_currency(String currency, Money otherMoney) {
        Double factor = convertion_table.get(otherMoney.currency).get(currency);
        return new Money(factor * otherMoney.amount, currency);
    }

    public static Money to_franc(Money money) {
        return to_currency("CHF", money);
    }

    public static Money to_dollar(Money money) {
        return to_currency("USD", money);
    }
}
