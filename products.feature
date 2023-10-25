# features/products.feature

Feature: Product Management

  Scenario: Read a product
    Given a product exists
    When I request the product
    Then I receive the product details

# Repeat for other scenarios
