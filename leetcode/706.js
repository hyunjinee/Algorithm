const MyHashSet = function () {
  this.hash = new Set([])
}

MyHashSet.prototype.add = function (key) {
  this.hash.add(key)
}

MyHashSet.prototype.remove = function (key) {
  this.hash.delete(key)
}

MyHashSet.prototype.contains = function (key) {
  return this.hash.has(key)
}
