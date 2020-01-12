package tests;

import model.Converter;
import model.Money;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

@DisplayName("Given a Converter")
public class ConverterTest {

    @Test
    @DisplayName("when 5 USD convert to 10 CHF")
    public void test_conversion() {
        Money five_dollars = Money.dollar(5);
        Money converted = Converter.to_franc(five_dollars);
        assertEquals(Money.franc(10), converted);
    }

    @Test
    @DisplayName("when 10 CHF convert to 5 USD")
    public void test_conversion_to_usd() {
        Money five_dollars = Money.franc(10);
        Money converted = Converter.to_dollar(five_dollars);
        assertEquals(Money.dollar(5), converted);
    }

}
