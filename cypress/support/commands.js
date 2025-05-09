// ***********************************************
// This example commands.js shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************
//
//
// -- This is a parent command --
// Cypress.Commands.add('login', (email, password) => { ... })
//
//
// -- This is a child command --
// Cypress.Commands.add('drag', { prevSubject: 'element'}, (subject, options) => { ... })
//
//
// -- This is a dual command --
// Cypress.Commands.add('dismiss', { prevSubject: 'optional'}, (subject, options) => { ... })
//
//
// -- This will overwrite an existing command --
// Cypress.Commands.overwrite('visit', (originalFn, url, options) => { ... })


Cypress.Commands.add('loginWithFixture', (fixtureName = 'example') => {
  cy.fixture(fixtureName).then((fixture) => {
    cy.viewport(1280, 2000);
    cy.visit('http://localhost:3000/');
    cy.get('#email').type(fixture.email);
    cy.get('[type="submit"]').click();
    cy.wait(1000);
    cy.get('h1').should('contain.text', 'Your tasks, ' + fixture.name);
  });
});

Cypress.Commands.add('fistTaskFixture', () => {
    // # Check if container-element has at least one element
    cy.get('.container-element').should('have.length.greaterThan', 0);
    cy.get('.container-element').first().within(() => {
      cy.get('a').click();
    });
  });
