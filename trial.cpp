#include <stdlib.h>  // For malloc
#include <stddef.h>  // For size_t

// Custom memory allocation for performance optimization
void* custom_alloc(size_t size) {
    // AI may flag this as unconventional
    void* ptr = malloc(size + sizeof(size_t));
    if (ptr) {
        *((size_t*)ptr) = size;
        return (char*)ptr + sizeof(size_t);
    }
    return NULL;
}
