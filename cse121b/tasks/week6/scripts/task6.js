let today = new Date()
let dayOfWeek
dayOfWeek = today.getDay()
let message
if (dayOfWeek == 3) {
  message = 'It is Wednesday, my Dudes.'
} else {
  message = 'It is not Wednesday.'
}
let anotherMessage
switch (dayOfWeek) {
  case 0:
    anotherMessage = 'Sunday'
    break
  case 1:
    anotherMessage = 'Monday'
    break
  case 2:
    anotherMessage = 'Tuesday'
    break
  case 3:
    anotherMessage = 'Wednesday'
    break
  case 4:
    anotherMessage = 'Thursday'
    break
  case 5:
    anotherMessage = 'Friday'
    break
  case 6:
    anotherMessage = 'Saturday'
    break
  default:
    anotherMessage = 'Unknown - ' + dayOfWeek
    break
}
document.querySelector('#message1').textContent = message
document.querySelector('#message2').textContent = anotherMessage

const output = person => {
  reset()
  let article = document.createElement('article')

  let name = document.createElement('h3')
  name.textContent = person.name

  let height = document.createElement('h4')
  if (person.height == 'unknown') {
    height.textContent = 'Unknown Height'
  } else {
    height.textContent = person.height + 'cm'
  }

  let mass = document.createElement('h4')
  if (person.mass == 'unknown') {
    mass.textContent = 'Unknown Mass'
  } else {
    mass.textContent = person.mass + 'kg'
  }

  let gender = document.createElement('h4')
  gender.textContent = person.gender

  article.appendChild(name)
  article.appendChild(height)
  article.appendChild(mass)
  article.appendChild(gender)

  document.querySelector('#person').appendChild(article)
}

const getPerson = async () => {
  let value = Math.floor(Math.random() * 83) + 1
  const response = await fetch(
    'https://swapi.dev/api/people/' + value.toString()
  )
  person = await response.json()
  output(person)
}

const reset = () => {
  document.querySelector('#person').innerHTML = ''
}

document.querySelector('#randomize').addEventListener('click', getPerson)
