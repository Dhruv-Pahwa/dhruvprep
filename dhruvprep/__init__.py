from .missing import handle_missing
from .outliers import remove_outliers_iqr
from .multicollinearity import calculate_vif, high_correlation
from .encoding import label_encode, one_hot_encode
from .scaling import standard_scale, minmax_scale
from .eda import basic_summary