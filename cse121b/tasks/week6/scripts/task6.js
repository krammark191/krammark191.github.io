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

const output = people => {
  people.forEach(person => {
    let article = document.createElement('article')

    let name = document.createElement('h3')
    name.textContent = person.name

    let mass = document.createElement('h4')
    mass.textContent = person.mass + "kg"

    let gender = document.createElement('h4')
    gender.textContent = person.gender

    article.appendChild(name)
    article.appendChild(mass)
    article.appendChild(gender)

    document.querySelector('#people').appendChild(article)
  })
}

const getPeople = async () => {
  const response = await fetch('https://swapi.dev/api/people')
  peopleList = await response.json()
  output(peopleList['results'])
}
getPeople()

const reset = () => {
  document.querySelector('#people').innerHTML = ''
}

const sortBy = () => {
  reset()

  let filter = document.querySelector('#sortBy').value

  switch (filter) {
    case 'ascending':
      output(
        peopleList.sort((person1, person2) => {
          let personName1 = person1.name.toLowerCase()
          let personName2 = person2.name.toLowerCase()
          if (personName1 < personName2) return -1
          else if (personName1 > personName2) return 1
          else return 0
        })
      )
      break
    case 'descending':
      output(
        peopleList.sort((person1, person2) => {
          let personName1 = person1.name.toLowerCase()
          let personName2 = person2.name.toLowerCase()
          if (personName1 > personName2) return -1
          else if (personName1 < personName2) return 1
          else return 0
        })
      )
      break
    default:
      output(
        peopleList.sort((person1, person2) =>
          person1.name.toLowerCase() > person2.name.toLowerCase()
            ? 1
            : person2.name.toLowerCase() >
              person1.name.toLowerCase()
            ? -1
            : 0
        )
      )
      break
  }
}

document.querySelector('#sortBy').addEventListener('change', sortBy)
