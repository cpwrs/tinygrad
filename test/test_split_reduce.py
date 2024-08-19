from tinygrad import Tensor
from tinygrad.codegen.kernel import Kernel, Opt, OptOps
from tinygrad.device import Buffer, Device
from tinygrad.shape.shapetracker import ShapeTracker
from tinygrad.shape.view import View
from tinygrad.dtype import dtypes

a = Tensor.rand(256,255).realize()
a = a.sum().numpy()
