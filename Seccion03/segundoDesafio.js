//Codigo original

function connectDatabase() {
    const didConnect = database.connect();
    if (didConnect) {
      return true;
    } else {
      console.log('Could not connect to database!');
      return false;
    }
  }
  
  function determineSupportAgent(ticket) {
    if (ticket.requestType === 'unknown') {
      return findStandardAgent();
    }
    return findAgentByRequestType(ticket.requestType);
  }
  
  function isValid(email, password) {
    if (!email.includes('@') || password.length < 7) {
      console.log('Invalid input!');
      return false;
    }
    return true;
  }

  //Codigo Personal

    
function connectDatabase() {
    const didConnect = database.connect();
    if (didConnect) {
      return true;
    } else {
      showError('Could not connect to database!');
      return false;
    }
  }

  function showError(message){
    console.log(message);
  }

  function determineSupportAgent(ticket) {
    if (ticket.requestType === 'unknown') {
      return findStandardAgent();
    }
    return findAgentByRequestType(ticket.requestType);
  }

  function validateEmail(email){
    if(!email.includes('@') || password.length < 7){
        showError('Invalid Input');
        return false;
    }else{
        return true;
    }
  }
  function validatePassword(password){
    if(password.length < 7){
        showError('Invalid Input');
        return false;
    }
    return true;
  }
  
  function isValid(email, password) {
    if (!validateEmail(email) || validatePassword(password)) {
      return false;
    }
    return true;
  }