package tests;

// using Junit5.4

import model.Dollar;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;


public class DollarTest {

    @Test
    public void given_5_Dollar_when_multiplied_by_2_than_result_10() {
        Dollar five = new Dollar(5);
        five.times(2);
        assertEquals(10, five.amount);
    }
}
