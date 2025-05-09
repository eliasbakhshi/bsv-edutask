// describe('R8UC1', () => {
//   let videoName = 'https://www.youtube.com/watch?v=bjh7EYdFTo4';
//   let taskName = '765RandomTaskName435345';

//   beforeEach('loadfixture', () => {
//     cy.loginWithFixture(); 
//     cy.fistTaskFixture();
//   });

//   it("Empty field and disable button", () => {
//     cy.get('form.submit-form').within(() => {
//       cy.get('input#title[name="title"]').should('be.empty');
//       cy.get('[type="submit"]').should('be.disabled');
//       cy.get('input#title[name="title"]').type('Say hello to the world man haha.');
//       cy.get('[type="submit"]').should('not.be.disabled');
//       cy.get('input#title[name="title"]').clear();
//       cy.get('[type="submit"]').should('be.disabled');
//     });
//   })

//   it('Add todo task', () => {
//     // # Check first if the task is already present
//     // cy.contains(taskName).should('not.exist');
//     cy.get('form.submit-form').within(() => {
//       cy.get('input[name="title"]').should('be.empty');
//       cy.get('input[name="title"]').type(taskName);
//       cy.get('input[name="url"]').should('be.empty');
//       cy.get('input[name="url"]').type(videoName);
//       cy.get('[type="submit"]').click();
//     })
//     
//   });
// });  

describe('R8UC1', () => {
  let videoName = 'https://www.youtube.com/watch?v=bjh7EYdFTo4';
  let taskName = '765RandomTaskName435345';

  beforeEach('loadfixture', () => {
    cy.loginWithFixture(); 
    cy.fistTaskFixture();
  });

  it("Empty field and disable button", () => {
    cy.get('form.inline-form').within(() => {
      cy.get('[type="text"]').clear();
      cy.get('[type="submit"]').should('be.disabled');
    });
  })

  it("Write something and not disable button", () => {
    cy.get('form.inline-form').within(() => {
      cy.get('[type="text"]').type(taskName);
      cy.get('[type="submit"]').should('not.be.disabled');
    });
  })

  it("Todo can be added at the end of the todo list", () => {
    // cy.viewport(1280, 2000);
    cy.get('form.inline-form').within(() => {
      cy.get('[type="text"]').type(taskName);
      cy.get('[type="submit"]').click();
    });
    // # Check if the task is added to the list
    cy.get('li.todo-item').last().within(() => {
      cy.contains(taskName, { timeout: 2000 }).should('exist');
    });
  })
});

describe('R8UC2', () => {
  beforeEach('loadfixture', () => {
    cy.loginWithFixture();
    cy.fistTaskFixture();
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
    cy.loginWithFixture(); 
    cy.fistTaskFixture(); 
  });

  it('Remove todo task', () => {
    let todoName = "Do this task";

    // # Add a new todo task
    cy.get('form.inline-form').within(() => {
      cy.get('input[type="text"]').type(todoName);
      cy.get('input[type="submit"]').click();
    })
    // # Check if the task is added to the list
    cy.contains('.todo-item', todoName).within(() => {
      cy.get('.remover').click()
    });
    // # Check if the task is removed from the list
    cy.contains('.todo-item', todoName).should('not.exist');
  })
})

