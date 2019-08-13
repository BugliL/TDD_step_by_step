package tests;

import model.Money;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

@DisplayName("Given dollars and francs")
public class MoneyTest {

    @Test
    @DisplayName("when compared 5USD and 5UHD result different")
    public void test_money_equality() {
        Money dollar = Money.dollar(5);
        Money franc = Money.franc(5);
        assertNotEquals(dollar, franc);
    }

    @Test
    @DisplayName("when get dollar Currency is USD")
    public void test_dollar_currency() {
        Money dollar = Money.dollar(10);
        assertEquals("USD", dollar.currency());
    }

    @Test
    @DisplayName("when get dollar Currency is CHF")
    public void test_franc_currency() {
        Money franc = Money.franc(10);
        assertEquals("CHF", franc.currency());
    }

    @Test
    @DisplayName("when get Money with Currency CHF are equals to franc")
    public void test_franc_created_money_currency() {
        Money franc = Money.franc(10);
        assertEquals(new Money(10, "CHF"), franc);
    }

    @Test
    @DisplayName("when get Money with Currency USA are equals to franc")
    public void test_dollar_created_money_currency() {
        Money dollar = Money.dollar(10);
        assertEquals(new Money(10, "USD"), dollar);
        assertNotEquals(new Money(10, "CHF"), dollar);
    }
}
