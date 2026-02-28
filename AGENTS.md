# AGENTS.md - AI Coding Agent Guidelines

These guidelines are designed to ensure the development and maintenance of this repository for AI coding agents. Adherence to these principles is crucial for maintaining code quality, reliability, and maintainability.

**1. DRY (Don't Repeat Yourself)**

*   All code should be reusable and avoid duplication.
*   When a function or class is defined, it should have a single, well-defined purpose.
*   Refactor any code segments that are logically related to minimize redundancy.
*   Leverage existing components and libraries when appropriate, but avoid unnecessary reimplementation.

**2. KISS (Keep It Simple, Stupid)**

*   Code should be as concise and understandable as possible.
*   Prioritize clarity over cleverness.
*   Avoid overly complex logic or abstractions unless absolutely necessary.
*   Strive for maximum readability.

**3. SOLID Principles**

*   **Single Responsibility Principle:** Each class/module should have one, and only one, reason to change.
*   **Open/Closed Principle:**  The system should be extensible through options without modifying the core implementation.  (Existing functionality should remain unchanged).
*   **Liskov Substitution Principle:**  Subclasses should be substitutable for their base classes without altering the correctness of the program.
*   **Interface Segregation Principle:**  Clients should not be forced to implement interfaces they do not use.
*   **Dependency Inversion Principle:**  High-level modules should be replaced by low-level modules that they depend on.

**4. YAGNI (You Aren't Gonna Need It)**

*   Implement only the functionality strictly required for the current task.
*   Avoid adding features that are not currently needed.
*   Refactor code to remove unused or unnecessary components.

**5. Code Length Constraint:**

*   Each file must not exceed 180 lines of code.
*   Code should be well-formatted and indented consistently.
*   Use appropriate whitespace for readability.

**6. Test Coverage Requirements:**

*   All code must achieve at least 80% test coverage.
*   Unit tests must cover all critical functionalities.
*   Integration tests must verify interactions between components.
*   Test design should be thorough and comprehensive.  Include edge case testing.

**7. Development Workflow & Best Practices:**

*   **Code Reviews:** Mandatory code reviews for all changes. Peer review is encouraged.
*   **Small, Focused Units:**  Break down large tasks into smaller, manageable units of code.
*   **Documentation:**  Write clear and concise documentation for all functions, classes, and modules. Explain parameters, return values, and potential side effects.
*   **Error Handling:** Implement appropriate error handling and logging.
*   **Version Control:** Utilize Git for version control and collaboration.
*   **Dependency Management:** Employ a dependency management system (e.g., Poetry, Pipenv) to manage external libraries.

**8. Specific Guidelines for AGENTS.md:**

*   **Component Definitions:** Clearly define each agent component with its responsibilities, inputs, and outputs.
*   **Data Structures:** Use appropriate data structures for representing agent state and data.
*   **Communication Protocols:** Establish clear communication protocols between agents (e.g., message queues, event streams).
*   **Security Considerations:**  Incorporate security best practices, especially regarding data privacy and access control.
*   **Logging:** Implement comprehensive logging to track agent actions and errors.

**9.  Testing Frameworks:**

*   Utilize a testing framework (e.g., pytest, unittest) for automated testing.
*   Write tests that cover all critical functionalities and edge cases.

**10.  Reporting:**

*   Maintain a detailed log of all development activities, including code commits, tests executed, and issues reported.
*   Regularly report on code coverage and testing results.

These guidelines are intended to guide the development of the AGENTS.md repository and ensure the creation of a robust, maintainable, and reliable AI coding agent system.