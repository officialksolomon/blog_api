async function getPosts (url) {
  let posts = await (await fetch(url)).json()
  return posts
}

console.log(getPosts('http://127.0.0.1:8000/api/posts/'));