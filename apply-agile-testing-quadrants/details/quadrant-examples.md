# Agile Testing Quadrant Examples

The Agile Testing Quadrants help teams ensure they are thinking about all aspects of testing. Below are examples of the types of tests that fall into each quadrant.

## Quadrant 1: Technology-facing tests that support the team
*Focus: Internal quality, test-driven development, fast feedback for developers.*

- **Unit Tests:** Testing individual classes or functions in isolation.
- **Component Tests:** Testing the interaction between a few closely related components.
- **API Tests:** Validating the endpoints of internal microservices.

## Quadrant 2: Business-facing tests that support the team
*Focus: External quality, business requirements, behavior-driven development.*

- **Functional Tests:** Validating that the software does what the business expects (e.g., Cucumber/SpecFlow scenarios).
- **Story Tests / Acceptance Tests:** Automated or manual checks of the acceptance criteria defined in a user story.
- **UI Prototyping / Wireframes:** Validating the user flow before building it.
- **Simulation:** Testing with mocks or stubs to verify complex business rules.

## Quadrant 3: Business-facing tests that critique the product
*Focus: Discovering the unknown, user experience, evaluating the working product.*

- **Exploratory Testing:** Unscripted, time-boxed testing to learn about the system and find edge cases.
- **Usability Testing:** Observing real users navigating the software to identify friction points.
- **User Acceptance Testing (UAT):** Final validation by the customer or product owner.
- **A/B Testing:** Comparing two versions of a feature to see which performs better with users.

## Quadrant 4: Technology-facing tests that critique the product
*Focus: Non-functional requirements, stability, security, architecture.*

- **Performance & Load Testing:** Verifying the system can handle expected (and unexpected) traffic.
- **Security Testing:** Penetration testing, vulnerability scanning, and threat modeling.
- **Maintainability Testing:** Static analysis, code complexity metrics, and architectural fitness functions.
- **Data Migration Testing:** Ensuring data integrity when moving or upgrading databases.
