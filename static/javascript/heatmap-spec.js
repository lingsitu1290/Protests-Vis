describe("My Test Suite", function () {

    // Testing getArrayOfDates function to expect first index 
    it("should get dates array", function () {
        var arrayOfDates = getArrayOfDates();
        expect(getArrayOfDates[0]).toBe(20160101);
    });

    // Test clearMap function to return empty list
    it("should get empty list", function () {
        var arrayOfDates = clearMap();
        expect(clearMap()).toBe([]);
    });
});