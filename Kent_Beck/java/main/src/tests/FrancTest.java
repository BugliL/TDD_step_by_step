package tests;

// using Junit5.4

import model.Dollar;
import model.Franc;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class FrancTest {

    @Test
    public void given_5_Dollar_when_multiplied_by_3_and_2_than_result_15() {
        Franc five = new Franc(5);
        Franc ten = five.times(2);
        assertEquals(new Franc(10), ten);
        Franc fifthteen = five.times(3);
        assertEquals(new Franc(15), fifthteen);
    }

    @Test
    public void given_2_dollers_of_same_amount_when_compared_result_equal() {
        assertEquals(new Franc(5), new Franc(5));
        assertNotEquals(new Franc(5), new Franc(15));
    }

}
