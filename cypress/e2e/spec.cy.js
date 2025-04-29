describe('template spec', () => {

  beforeEach(() => {
    cy.visit('https://davidallert.github.io/stenrik/#karta')
  })
  it('Menu contains Karta', () => {
    cy.get('#hamburgerMenuBtn').click()
    cy.contains('Karta')
  });

  it('Menu contains Logga in', () => {
    cy.get('#hamburgerMenuBtn').click()
    cy.contains('Logga in').click()
  });
})