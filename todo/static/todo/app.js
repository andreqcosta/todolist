const cardBtns = document.querySelectorAll('#card-btn')


for (let i = 0; i < cardBtns.length; i++) {
    let parent = cardBtns[i].parentElement

    setDone(cardBtns[i], parent)

    cardBtns[i].addEventListener('click', (e) => changeDone(cardBtns[i], parent))
    
}

function setDone(button, parent) {
    console.log(button)
    if (button.value == 'True') {
        parent.style.backgroundColor = "rgb(50, 200, 50)"
        button.textContent = "Done"
    }else{
        parent.style.backgroundColor = "rgb(200, 50, 50)"
        button.textContent = "To Do"
    }
}