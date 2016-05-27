

## This function creates a special "matrix" object that can cache its inverse

makeCacheMatrix <- function(x = matrix()) {
  inv_x<-NULL
  set<-function(y){
    x<<-y
    inv_x<<-NULL
  }
  get<-function() x
  setinverse<-function(inverse) 
    inv_x <<- inverse
  getinverse<-function() 
    inv_x
  list(set=set, get=get,
       setinverse=setinverse,
       getinverse=getinverse)
}


## This function computes the inverse of the special "matrix" 
## returned by makeCacheMatrix above.

cacheSolve <- function(x, ...) {
  inv_x<-x$getinverse()
  if(!is.null(inv_x)){
    message("getting cached data")
    return(inv_x)
  }
  else{
    inv_x<-solve(x$get())
    x$setinverse(inv_x)
  }
  inv_x
  ## Return a matrix that is the inverse of 'x'
}