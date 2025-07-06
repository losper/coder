#include <gtest/gtest.h>
#include "../src/foo.h"

TEST(AddTest, PositiveNumbers) {
    EXPECT_EQ(add(1, 2), 3);
    EXPECT_EQ(add(5, 7), 12);
}

TEST(AddTest, NegativeNumbers) {
    EXPECT_EQ(add(-1, -2), -3);
    EXPECT_EQ(add(-5, 7), 2);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
