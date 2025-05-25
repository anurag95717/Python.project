let todolist = [{item:'Buy Milk',duedate:'4/9/2025'},{item:'go to collage',duedate:'4/9/2025'}]
displayItem()
function addTodo(){
    let inputElement = document.querySelector('#todo-input')
    let dateElement = document.querySelector('#todo-date')
    let todoItem = inputElement.value
    let tododate=dateElement.value
    todolist.push({item:todoItem,duedate:tododate})
    inputElement.value=''
    dateElement.value=''
    displayItem();
}
function displayItem(){
    let containerElement = document.querySelector
    ('.todo-container')
    let newHtml = '';
    for (let i=0; i<todolist.length;i++){
        let {item,duedate}=todolist[i]
      newHtml += `
           
            <span>${item}</span>
            <span>${duedate}</span>
            <button class='button-delete' onclick='todolist.splice(${i}, 1) ;
            displayItem()'>Delete</button>
          
      `;
        
    }
    containerElement.innerHTML=newHtml;
}