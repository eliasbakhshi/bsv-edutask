describe('R8UC1', () => {
  let videoName = 'https://www.youtube.com/watch?v=bjh7EYdFTo4';
  let taskName = '765RandomTaskName435345';

  beforeEach('loadfixture', () => {
    cy.loginWithFixture(); // Use the custom command
  });

  it("Empty field and disable button", () => {
    cy.get('form.submit-form').within(() => {
      cy.get('input#title[name="title"]').should('be.empty');
      cy.get('[type="submit"]').should('be.disabled');
      cy.get('input#title[name="title"]').type('Say hello to the world man haha.');
      cy.get('[type="submit"]').should('not.be.disabled');
      cy.get('input#title[name="title"]').clear();
      cy.get('[type="submit"]').should('be.disabled');
    });
  })

  it('Add todo task', () => {
    // # Check first if the task is already present
    // cy.contains(taskName).should('not.exist');
    cy.get('form.submit-form').within(() => {
      cy.get('input[name="title"]').should('be.empty');
      cy.get('input[name="title"]').type(taskName);
      cy.get('input[name="url"]').should('be.empty');
      cy.get('input[name="url"]').type(videoName);
      cy.get('[type="submit"]').click();
    })
    // # Check if the task is added to the list
    cy.get('.container-element').eq(-2).within(() => {
      cy.contains(taskName, { timeout: 2000 }).should('exist');
    });
  });
});

describe('R8UC2', () => {
  beforeEach('loadfixture', () => {
    cy.loginWithFixture(); // Use the custom command
    // # Check if container-element has at least one element
    cy.get('.container-element').should('have.length.greaterThan', 0);
    cy.get('.container-element').first().within(() => {
      cy.get('a').click();
    });
  });

  it('Set todo task as active', () => {
    cy.get('.todo-item').first().within(() => {
      // # Check if the task is not checked if it is, then uncheck it
      cy.get('.checker').then(($el) => {
        const classList = $el.attr('class');
        if (!classList.includes('unchecked')) { 
          cy.wrap($el).click();
        }
        cy.wrap($el).should('have.attr', 'class').and('contain', 'unchecked');
        cy.get('.editable').should('not.have.css', 'text-decoration-line', 'line-through');
      })
      })
  })
  
  it('Set todo task as done', () => {
    cy.get('.todo-item').first().within(() => {
      cy.get('.checker').then(($el) => {
        const classList = $el.attr('class');
        if (classList.includes('unchecked')) {
          cy.wrap($el).click();
        }
        cy.wrap($el).should('have.attr', 'class').and('contain', 'checked');
        cy.get('.editable').should('have.css', 'text-decoration-line', 'line-through');
      })
      })
  })
})

describe('R8UC3', () => {

  beforeEach('loadfixture', () => {
    cy.loginWithFixture(); // Use the custom command
    // # Check if container-element has at least one element
    cy.get('.container-element').should('have.length.greaterThan', 0);
    cy.get('.container-element').first().within(() => {
      cy.get('a').click();
    });
    
  });

  it('Remove todo task', () => {
    let todoName = "Do this task";

    // # Add a new todo task
    cy.get('form.inline-form').within(() => {
      cy.get('input[type="text"]').should('be.empty');
      cy.get('input[type="text"]').type(todoName);
      cy.get('input[type="submit"]').click();
    })
    // # Check if the task is added to the list
    cy.contains('.todo-item', todoName).within(() => {
      cy.get('.remover').click()
      // cy.get('.remover').click().click();
  });
    // # Check if the task is removed from the list
    cy.contains('.todo-item', todoName).should('not.exist');

      // # Check if the task is not checked if it is, then uncheck it
    // cy.get('.remover').then(($el) => {
    //   cy.wrap($el).click();
    // })

    // // # Check if the task is removed from the list
    // cy.get('.todo-item').should('not.exist');
    // cy.get('.todo-item').within(() => {
    //   cy.contains(todoName, { timeout: 2000 }).should('not.exist');
    // });
  })
})

