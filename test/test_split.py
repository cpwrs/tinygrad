(UOp(UOps.SINK, None, arg=None, src=(
  UOp(UOps.STORE, None, arg=None, src=(
    UOp(UOps.DEFINE_GLOBAL, PtrDType(dtypes.float), arg=0, src=()),
    UOp(UOps.SHAPETRACKER, None, arg=ShapeTracker(views=(View(shape=(1, 1), strides=(0, 0), offset=0,
mask=None, contiguous=True),)), src=()),
    UOp(UOps.REDUCE_AXIS, dtypes.float, arg=(ReduceOps.SUM, (0, 1)), src=(
      UOp(UOps.LOAD, dtypes.float, arg=None, src=(
        UOp(UOps.DEFINE_GLOBAL, PtrDType(dtypes.float), arg=1, src=()),
        UOp(UOps.SHAPETRACKER, None, arg=ShapeTracker(views=(View(shape=(256, 255), strides=(255, 1),
offset=0, mask=None, contiguous=True),)), src=()),)),)),)),)), [])
