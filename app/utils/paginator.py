from sqlalchemy.sql import select
import math

def paginate(query: select, page: int, items: int):
  offset = (page - 1) * items
  count = query.count()
  return count, query.offset(offset).limit(items).all(), math.ceil(count / items)

def set_pagination_headers(response, count, pages, page, items):
  response.headers['X-Total-Count'] = str(count)
  response.headers['X-Total-Pages'] = str(pages)
  response.headers['X-Current-Page'] = str(page)
  response.headers['X-Per-Page'] = str(items)