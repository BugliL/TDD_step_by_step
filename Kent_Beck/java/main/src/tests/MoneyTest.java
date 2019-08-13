package tests;

import model.Dollar;
import model.Franc;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotEquals;

@DisplayName("Given dollars and francs")
public class MoneyTest {

    @Test
    @DisplayName("when compared 5USD and 5UHD result different")
    public void test_money_equality() {
        Dollar dollar = new Dollar(5);
        Franc franc = new Franc(5);
        assertNotEquals(dollar, franc);
    }
}
