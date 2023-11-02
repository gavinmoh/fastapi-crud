def sort(query, sort_by, sort_order):
  if sort_by is None or sort_order is None:
    return query
  if sort_order == 'desc':
    return query.order_by(getattr(query.column_descriptions[0]['entity'], sort_by).desc())
  return query.order_by(getattr(query.column_descriptions[0]['entity'], sort_by).asc())